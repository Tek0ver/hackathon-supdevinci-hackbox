<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Machine;

class Client extends Model
{
    use HasFactory;
    protected $table = 'client';

    // Relation entre Client et Machine : Un client peut avoir plusieurs machines
    public function machines()
    {
        return $this->hasMany(Machine::class);
    }
}
