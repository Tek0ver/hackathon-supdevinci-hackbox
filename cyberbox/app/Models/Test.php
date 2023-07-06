<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Machine;

class Test extends Model
{
    use HasFactory;

    protected $table = 'test';

    // Relation entre Test et Machine : Un test appartient à une machine
    public function machine()
    {
        return $this->belongsTo(Machine::class);
    }
}
